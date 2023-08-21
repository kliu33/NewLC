/**
 * @param {string} s
 * @return {string}
 */
var sortSentence = function(s) {
    let words = s.split(' ')
    let hash_map = {}
    for (let word of words){
        let end = word.length - 1
        hash_map[word[end]] = word.slice(0,end)
    }
    return Object.values(hash_map).join(" ")
};