function doesAliceWin(s: string): boolean {
  const vowels = ['a', 'e', 'i', 'o', 'u'];

  return s.split('').some(ch => vowels.includes(ch));
}
console.log(doesAliceWin("solution"));
console.log(doesAliceWin("der"));  
console.log(doesAliceWin("leetcoder"));  
console.log(doesAliceWin("checking"));  