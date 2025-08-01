/**
 * @param {number} numRows
 * @return {number[][]}
 */
var generate = function(numRows) {
    tri = setup(numRows)
    console.log(tri)
    for(let i =1; i<tri.length-1; i++)
    {
        for(let j = 0; j<tri[i].length-1; j++)
        {
            tri[i+1][j+1] = tri[i][j] + tri[i][j+1]
        }
    }
    return tri
};
var setup=(rows)=>{
    let arr = []
    for(let i = 1; i<=rows;i++)
    {
        let lst = new Array(i)
        lst[0]=1
        lst[i-1]=1
        arr.push(lst)
    }
    return arr
}