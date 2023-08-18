/**
 * @param {string} s
 * @return {number}
 */
var balancedStringSplit = function(s) {
    let out = 0;
    let rcount = 0;
    let lcount = 0;
    for (let i = 0; i < s.length; i++){
        if (s[i] === 'L'){
            lcount++;
        } else {
            rcount++;
        }
        if (lcount === rcount){
            out ++;
            lcount = 0;
            rcount = 0;
        }
    }
    return out;
};