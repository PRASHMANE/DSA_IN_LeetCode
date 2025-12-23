class Solution {
    public boolean isPathCrossing(String path) {
        int x=0,y=0;
        List <String> visited = new ArrayList<>();
        visited.add("0,0");

        for(char c : path.toCharArray()){
            if (c == 'N') y++;
            else if (c == 'S') y--;
            else if (c == 'E') x++;
            else x--;

            String pos = x+","+y;
            if (visited.contains(pos)){
                return true;
            }
            visited.add(pos);
        }
        return false;
        
    }
}