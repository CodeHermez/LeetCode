/**
 * @param {string} s
 * @return {number}
 */
function maxFreqSum(s) {
  var vowels = new Set(['a', 'e', 'i', 'o', 'u']);
  var freq = new Array(26).fill(0);

  for (let i = 0; i < s.length; i++) {
    freq[s.charCodeAt(i) - 97]++;
  }
  
  let mx_v = 0;
  let con_st = 0;
  for (let i = 0; i < 26; i++) {
    const char = String.fromCharCode(i + 97);
    if (vowels.has(char)) {
      mx_v = Math.max(mx_v, freq[i]);
    } else {
      con_st = Math.max(con_st, freq[i]);
    }
  }

  return mx_v + con_st;
}
