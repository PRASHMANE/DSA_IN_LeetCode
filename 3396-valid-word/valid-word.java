class Solution {
    public boolean isValid(String word) {
        if (word.length() < 3) return false;

        String vowels = "aeiouAEIOU";
        int v = 0, c = 0;

        for (char ch : word.toCharArray()) {
            if (!Character.isLetterOrDigit(ch))
                return false;

            if (Character.isLetter(ch)) {
                if (vowels.indexOf(ch) != -1)
                    v++;
                else
                    c++;
            }
        }
        return v > 0 && c > 0;
    }
}
