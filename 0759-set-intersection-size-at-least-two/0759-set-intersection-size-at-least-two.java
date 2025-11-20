class Solution {
    public int intersectionSizeTwo(int[][] intervals) {
        Arrays.sort(intervals, (frst, sup) -> {
            if (frst[1] == sup[1]) return sup[0] - frst[0];
            return frst[1] - sup[1];
        });

        List<Integer> vals = new ArrayList<>();
        for (int[] c : intervals) {
            int ini = c[0], end = c[1];
            int counter = 0;
            for (int x : vals) {
                if (x >= ini && x <= end) counter++;
            }

            if (counter == 0) {
                vals.add(end - 1);
                vals.add(end);
            } else if (counter == 1) {
                vals.add(end);
            }
        }

        return vals.size();
    }
}
