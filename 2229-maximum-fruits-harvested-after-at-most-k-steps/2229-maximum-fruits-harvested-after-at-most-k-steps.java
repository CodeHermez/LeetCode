class Solution {
    boolean feasable(int sp, int k, int[][]fruits, int l, int r)
    {
        int lp=fruits[l][0],rp=fruits[r][0],tk=0;
        tk = lp-sp;
        boolean check= k >= Math.min(
            Math.abs(sp-lp)+(rp-lp),
            Math.abs(sp-rp)+(rp-lp));
            
            System.out.println(check);

        return check;
    }
    public int maxTotalFruits(int[][] fruits, int startPos, int k) {
        int sum=0,l=0,s=0;
        for(int i=0; i<fruits.length; i++)
        {
            s = s + fruits[i][1];
            for(;l<=i && !feasable(startPos,k,fruits,l,i);)
            {
                s = s - fruits[l][1];
                l++;
            }
            sum = Math.max(sum,s);
        }
        System.out.println(sum);
        return sum;
    }
}