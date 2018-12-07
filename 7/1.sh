function solve {
  sed 's/Step //;s/ must be finished before step / /;s/ can begin.//' $1 | tsort
}

solve test.in | paste -sd ' ' -
solve puzzle.in | paste -sd ' ' -
