class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        // create a frequency bucket list of lists where highest index is nums.length
        // create a map with the count of each number in the nums list
        // get frequency at every map entry's value and add map entry's key to the list
        // create a int[] result array fo size k
        // iterate through frequency until result index == k, start at the end of frequency
        // iterate through the list at freq[i] then move to next list
        // increment res index as needed

        List<Integer>[] freq = new List[nums.length + 1];
        for(int i = 0; i < freq.length; ++i) {
            freq[i] = new ArrayList<>();
        }

        Map<Integer, Integer> count = new HashMap<>();
        for(int num : nums) {
            count.put(num, count.getOrDefault(num, 0) + 1);
        }

        for(Map.Entry<Integer, Integer> entry : count.entrySet()) {
            freq[entry.getValue()].add(entry.getKey());
        }

        int[] res = new int[k];
        int j = 0;
        for(int i = freq.length - 1; i > 0; --i) {
            for(int num : freq[i]) {
                res[j] = num;
                ++j;
                if(j == k) return res;
            }
        }

        return res;
       
    }
}
