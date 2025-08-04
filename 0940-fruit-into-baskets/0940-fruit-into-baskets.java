class Solution {
    // public int totalFruit(int[] fruits) {
    //     int[] arr = new int[fruits.length];
    //     int lrgst,secndlrgest,sum;
    //     System.out.println(arr.length);
    //     System.out.println(arr[0]);
    //     for(int i=0;i<fruits.length;i++)
    //     {
    //         arr[fruits[i]] +=1;
    //     }
    //     lrgst = largest(arr);
    //     sum = arr[lrgst];
    //     printArray(arr);
    //     arr[lrgst] = -1;
    //     secndlrgest = largest(arr);
    //     sum+=arr[secndlrgest];
    //     printArray(arr);
    //     System.out.println("sum: "+sum);
    //     return sum;
    // }

    void printArray(int [] arr)
    {
        System.out.print('[');
        for(int i=0;i<arr.length;i++)
        {
            System.out.print(arr[i]+",");
        }
        System.out.println(']');
    }
    int largest(int [] arr)
    {
        int largest = -100,index=-1;
        for(int i=0; i<arr.length; i++)
        {
            if(arr[i]>largest)
            {    
                largest = arr[i];
                index = i;
            }
        }
        return index;
    }

    public int totalFruit(int[] fruits) {
        Map<Integer,Integer> arr = new HashMap<>();
        int l,r,sum;
        l=r=sum=0;
        while(r<fruits.length)
        {
            int frt = fruits[r];
            arr.put(frt,arr.getOrDefault(frt,0)+1);
            while(arr.size()>2)
            {
                int lf=fruits[l];
                arr.put(lf,arr.get(lf)-1);
                if(arr.get(lf)==0)
                    arr.remove(lf);
                l++;
            }
            sum=Math.max(sum,r-l+1);
            r++;
        }
        return sum;
    }

}