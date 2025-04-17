### Generating Compiled library
To run some of the machine learning python files, it is necessary to have a compiled library of some dictionaries.
You can generate the libraries by running the following commands:

```bash
    rootcling -f DictDict.cxx -c DictTypes.h LinkDef.h

```
```bash
    g++ -fPIC -shared DictDict.cxx -o libdict.so $(root-config --cflags --libs)

```

It is important to mention that the vdt math library is required to compile the files. 
Here's the link to the library's github page:

https://github.com/dpiparo/vdt 
