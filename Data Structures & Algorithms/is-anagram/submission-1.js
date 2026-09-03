class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }

        let infoS = {};
        let infoT = {};
        for (let i = 0; i < s.length; i++) {
            if (!Object.hasOwn(infoS, s[i])) {
                infoS[s[i]] = 1;
            } else {
                infoS[s[i]] += 1;
            }
        }

        for (let i = 0; i < t.length; i++) {
            if (!Object.hasOwn(infoT, t[i])) {
                infoT[t[i]] = 1;
            } else {
                infoT[t[i]] += 1;
            }
        }

        if (Object.keys(infoS).length !== Object.keys(infoT).length) {
            return false;
        } else {
            for (const key in infoS) {
                console.log(infoT[key], infoS[key])
                if (infoT[key] !== infoS[key]) {
                    return false;
                }
            }
        }
        return true;
    }
}
