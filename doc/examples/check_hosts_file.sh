#!/bin/bash

# this script uses reach to check /etc/hosts and demonstrates:
# - reach
# - reading a file
# - output redirection
# - bash arrays

# which file should we check?
declare input_file=/etc/hosts
declare unreachable_file=/tmp/hosts.unreachable_ips
declare unknown_errors_file=/tmp/hosts.unknown_errors
declare error_separator="================="
declare error=""
declare _rc=0
declare line_num=0
declare record_num=0

function check_reachability() {
  #echo "checking $1" >&2
  error=$(reach $1 2>&1)
  _rc=$?
  if [[ $_rc -eq 1 ]]; then
    echo $1 >> $unreachable_file
    _rc=3
  elif [[ $_rc -eq 2 ]]; then
    {
    echo 'strange error for entry: "'$1'" from line number '$line_num
    echo $error 
    echo $error_separator
    } >> $unknown_errors_file
    _rc=3
  fi
  return $_rc
}

# open file
[[ -t 3 ]]           && { echo "ERROR: file descriptor 3 already open."; exit 255; } >&2
[[ -r $input_file ]] || { echo "ERROR: $input_file missing or unreadable"; exit 1; } >&2
exec 3< $input_file  || { echo "ERROR: Failed to open $input_file"; exit 255; } >&2

# truncate output files with a noop
: > $unreachable_file || { 
	echo "ERROR: Failed to truncate $unreachable_file"; 
	exit 255; 
	} >&2
: > $unknown_errors_file || { 
	echo "ERROR: Failed to touch or truncate $unknown_errors_file"; 
	exit 255; 
	} >&2

while read <&3; do
  # increment line count
  line_num=$(( line_num + 1 ))

  # ignore blank lines
  grep -q '^[[:space:]]*$' <<< $REPLY && continue

  # ignore comments
  grep -q '^[[:space:]]*#' <<< $REPLY && continue

  # convert the line into an array
  # see http://tldp.org/LDP/abs/html/arrays.html
  # on how to use 1-dimensional arrays
  record=( $REPLY )

  # increment record_num
  record_num=$(( record_num + 1 ))

  # attempt to reach ip
  check_reachability ${record[0]}

  #
done

# close file
exec 3<&- || exit 255

echo "Checked $record_num records"
echo -n "Unreachable IPs: "; wc -l  $unreachable_file 
echo -n "Unknown errors:  "; grep -c "$error_separator" $unknown_errors_file | tr '\n' ' '; echo $unknown_errors_file

exit $_rc
