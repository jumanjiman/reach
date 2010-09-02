#!/bin/bash

. /etc/reach/functions

# test cases
tests="
127.0.0.1

blah.blah.blah.blah
::1
"

for test in $tests; do
  echo -n "ipv4 $test : "
  is_ipv4 $test && echo true || echo false
  echo -n " : "
  is_ipv4       && echo true || echo false
  echo -n "ipv6 $test : "
  is_ipv6 $test && echo true || echo false
done
