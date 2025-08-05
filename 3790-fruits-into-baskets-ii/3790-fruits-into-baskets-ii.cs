public class Solution {
    public int NumOfUnplacedFruits(int[] fruits, int[] baskets) {
        // Dictionary<int,int>map = new Dictionary<int,int>();
        // int counter = 0;
        // for(int i=0; i<fruits.Length; i++){
        //     for(int j = 0; j<fruits.Length;j++)
        //     {
        //         if(fruits[i]<=baskets[j] && !map.ContainsKey(baskets[j]))
        //         {
        //             map.Add(baskets[j],fruits[i]);
        //             fruits[i] = -1;
        //             break;
        //         }
        //         else if(map.ContainsKey(baskets[j]) && map[baskets[j]]==fruits[i])
        //             fruits[i] = -1;
        //     }
        // }
        // Console.Write("{");
        // for(int i=0; i<fruits.Length; i++){
        //     if(fruits[i] != -1)
        //         counter++;
        //     Console.Write(fruits[i] + ", ");
        // }
        // Console.Write("}");

        // return counter;
        bool[]check = new bool[fruits.Length];
        int counter = 0;
        for(int i=0; i<fruits.Length;i++)
            for(int j=0;j<fruits.Length;j++)
                if(!check[j] && fruits[i]<=baskets[j])
                {
                    check[j]=true;
                    fruits[i]=-1;
                    break;
                }
        for(int i=0;i<fruits.Length;i++)
            if(fruits[i]!=-1)
                counter++;
        
        Console.Write("{");
        for(int i=0; i<fruits.Length; i++){
            Console.Write(fruits[i] + ", ");
        }
        Console.Write("}");
        return counter;
    }
}