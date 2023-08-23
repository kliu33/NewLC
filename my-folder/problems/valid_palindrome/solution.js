/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    return toLowerAlpha(s) == toLowerAlpha(s).split('').reverse().join('')
};

var toLowerAlpha = function(s) {
    let out = ""
    const alpha = "abcdefghijklmnopqrstuvwxyz01234567689"
    for (let char of s){
        if (alpha.includes(char.toLowerCase())) {
            out += char.toLowerCase();
        }
    }
    return out
}