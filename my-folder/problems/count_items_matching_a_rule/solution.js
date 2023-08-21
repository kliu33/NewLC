/**
 * @param {string[][]} items
 * @param {string} ruleKey
 * @param {string} ruleValue
 * @return {number}
 */
var countMatches = function(items, ruleKey, ruleValue) {
    let out = 0;
    switch(ruleKey) {
        case 'type':
            for (let item of items){
                if (item[0] === ruleValue){
                    out++
                }
            }
            break;
        case 'color':
            for (let item of items){
                if (item[1] === ruleValue){
                    out++
                }
            }
            break;
        case 'name':
            for (let item of items){
                if (item[2] === ruleValue){
                    out++
                }
            }
            break;
        default:
            break;
    }
    return out
};