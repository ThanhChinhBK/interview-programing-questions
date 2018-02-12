#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
using namespace std;

struct Tag{
  Tag(string name, Tag *parent) : name(name), parent(parent)
  {
  }
  string name;
  map <string, Tag*> children;
  map <string, string> attributes;
  Tag *parent;
};

bool search(Tag *curScope, string line, string *result){
  string chunk;
  size_t pos = line.find(".");
  cerr << "Searching for " << line << " in " << curScope->name << endl;
  pos = line.find(".");
  if (pos == string::npos)
    pos = line.find("~");
  
  if(pos == string::npos){ // final children
     
    if(curScope->attributes.count(line) == 0)
      return false;
    *result = curScope->attributes[line];
    return true;
  }
  else{
    chunk = line.substr(0, pos);
    if (curScope->children.count(chunk) == 0)
      return false;
    return search(curScope->children[chunk], line.substr(pos+1), result);
  }

}

int main() {
  int n, q;
  Tag root("[root]", NULL);
  Tag *curScope = &root, *tag;
  size_t pos;
  string line, chunk, name, value;
  cin >> n >> q;
  getline(cin, line);
  for(int i = 0; i < n; i++){
    getline(cin, line);
    if (line.find("</") == 0)
      curScope = curScope -> parent;
    else{
      pos = line.find(" ");
      if (pos == string::npos)
        name = line.substr(1);
      else
        name = line.substr(1, pos - 1);
      if (name.back() == '>'){
        name = name.substr(0, name.length() - 1);
        tag = new Tag(name, curScope);
      }    
      else{
        line = line.substr(pos + 1);
        tag = new Tag(name, curScope);
        while(true){
          pos = line.find('\"');
          pos = line.find('\"', pos+1);
          chunk = line.substr(0, pos+1);
          line = line.substr(pos+1);
          name = chunk.substr(0, chunk.find(" "));
          pos = chunk.find("\"");
          value = chunk.substr(pos+1);
          value = value.substr(0, value.length() - 1);
          tag -> attributes[name] = value;

          if (line.front() == '>')
            break;
          else 
            line = line.substr(1);
        }
      }
      curScope->children[tag->name] = tag;
      curScope = tag;
    }

  }

  for (int i = 0; i < q; i++){
    getline(cin, line);
    if (line.find('~') == string::npos)
      cout << "Not Found!" << endl;
    else if (!search(&root, line, &value))
      cout << "Not Found!" << endl;
    else
      cout << value << endl;
  }
  return 0;
}

