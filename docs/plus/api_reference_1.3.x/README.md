# tool: doxy2md

To generate MD document from headers with doxygen comments

> **Warning** 
>
> - only limited doxygen syntax is supported
> - need to check the converted document 
>  - push to Kneron Document Center

## Usage
```bash
cd ci/doxy2md
python3 doxy2md.py ../../src/include/kdp_host.h    // follow mkdocs md format
python3 doxy2md.py -s ../../src/include/kdp_host.h // follow std md format

# kdp_host.h.md will be generated
```

> **notes**
> md syntax of links used for **mkdocs**
>```
>ex.  [xxxx](##typedef void *kdp2_device_t;)
>  -> [xxxx](#typedef-void-kdp2_device_t)
>
>1. ####             -> #
>2. .;()+*           -> remove
>3. space            -> -
>4. uppercase word   -> lower case word
>```

## Supported Syntax

### styles:


```c
#1: 
----
/**
 * @[doxygen keywords] ...
 */

#2: 
----
 ....  /**< comments .... */

```


### file header section

**@file** and **@brief** are **must**

```c
/**
 * @file xxxx.c
 * @brief one_line
 * 
 * // above blank line means the this line is the 1st line of @details //
 * // support multiple lines                  
 *                 
 * @details multiple lines    //another usage of @details
 */
```



### Define macro

comment is **must** for all `#define macro` for **value** or **name alias**
```c
#define macro value  /**< multiple 
                          lines of comment */
```
> **notes**
> no comment for **macro functions** is allowed  
> eg. `#define ABC(x) func(x)`
>
> no comment for **function pointer declearation** is allowed
> eg. `#define int (*xxx_cb)(int aaa, int bbb)`


### simple typedef 

This means type alias of simple value types 

**Exclude** typedef for **enum**, **struct**, **union**

```c
/**
 * @brief one_line description
 */
typedef void* type_alias_t;
```



### Enumulators

comment for enum elements are *optional*

```c
/**
 * @brief one_line descrition of enum
 */
enum example_e {
    index0=0,   /**< comment for index0 */
    index1      /**< comment for index1 */
};


/**
 * @brief one_line descrition of typedef enum
 */
typedef enum example_s {
    index0=0,   /**< comment for index0 */
    index1      /**< comment for index1 */
} example_t;
```



### Structures

Comments for all members are **must**

```c
/**
 * @brief one_line descrition of structure
 */
struct example_s {
    int member1;    /**< comment for member1 */
    int member2;    /**< comment for member2 */
};

/**
 * @brief one_line descrition of structure
 */
struct example_s {
    int member1;    /**< comment for member1 */
    int member2;    /**< comment for member2 */
} __attribute__(packed);

/**
 * @brief one_line descrition of typedef struct
 */
typedef struct example_s {
    int member1;    /**< comment for member1 */
    int member2;    /**< comment for member2 */
} example_t;

```



### unions

all members must have comments  

```c
/**
 * @brief one_line descrition of union
 */
union example_s {
    int member1;    /**< comment for member1 */
    int member2;    /**< comment for member2 */
};

/**
 * @brief one_line descrition of typedef union
 */
typedef union example_s {
    int member1;    /**< comment for member1 */
    int member2;    /**< comment for member2 */
} union_t;
```



### Functions

**@brief** is **must**

optional:

- others are optional
- direction, [in], [out], [in,out] are optional
  

```c
/**
 * @brief one line function description
 * @details multiple lines
 *
 * @param[in]       param_name      multiple lines description
 * @param[out]      param_name_xxx  multiple lines description
 * @param[in,out]   param_name_abc  multiple lines description
 *
 * @return 0 on succeed, error code on failure (one line)
 * @note multiple lines descrption
 */
int ex_func(int param_name, int param_xxx, int param_name_abc);
```
