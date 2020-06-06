class Solution {
    public List<List<String>> partition(String s) {
      List<List<String>> a=new ArrayList<>();
      part(s,a,new ArrayList<String>(),0);
      return a;
      
        
    }
  void part(String s,List<List<String>> a,List<String> ab,int i)
  {
    if(i==s.length())
    {
      a.add(new ArrayList<>(ab));
      return;
    }
    
    for(int j=i;j<s.length();j++)
    {
      if(pail(s,i,j))
      {
        ab.add(s.substring(i,j+1));
        part(s,a,ab,j+1);
        
        ab.remove(ab.size()-1);
      }
    }
  }
  boolean pail(String abc,int i,int j)
  {
    if(i>=j)
      return true;
    while(i<j)
    {
      if(abc.charAt(i)!=abc.charAt(j))
      {
        return false;
        
      }
      i++;
      j--;
    }
    return true;
  }
}
