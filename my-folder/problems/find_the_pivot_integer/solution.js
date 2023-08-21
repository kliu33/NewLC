/**
 * @param {number} n
 * @return {number}
 */
const sumOfRange = (l, r) => (l + r) * (r - l + 1) / 2;

const pivotInteger = (n) => {
    for (let x = 1; x <= n; x++) {
        if (sumOfRange(1, x) == sumOfRange(x, n)) return x;
    }
    return -1;
};