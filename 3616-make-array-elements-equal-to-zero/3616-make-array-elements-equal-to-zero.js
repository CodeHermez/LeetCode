/**
 * @param {number[]} nums
 * @return {number}
 */
var countValidSelections = function(nums) {
    var counter = 0
    for (var i=0; i<nums.length; i++)
    {
        if (nums[i]===0)
        {
            if (testing(i,-1,nums))
                counter+=1
            if (testing(i,1,nums))
                counter+=1
        }
    }
    return counter
};
let testing = (s,dr, n) =>{
    var hello = n.length,
    pos = s,
    list = structuredClone(n),
    LorR = dr

    while(0<=pos && pos<hello)
        if (list[pos]==0)
            pos += dr
        else
        {
            list[pos]-=1
            dr*=-1
            pos+=dr
        }
    return list.every(x => x===0)
} 