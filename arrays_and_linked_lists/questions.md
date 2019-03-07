1. Implement an algorithm to determine if a string has all unique characters.
```python

def are_all_chars_unique(given_str:str) -> bool:
    char_set: set = ({})
    for x in given_str:
        if x in char_set:
            return False
        else:
            char_set.add(x)

def are_all_chars_unique(given_str:str) -> bool:
    char_set: list = [False]*256
    for x in given_str:
        if char_set[ord(x)]:
            # seen already
            return False
        else:
            char_set[ord(x)] = True
```
What if we can't use additional storage?
- compare each with each
- sort and compare ajacent


2. Given two strings, find if one is a permutation of the other.
```python
from typing import List
def is_string_pair_perm(str1:str, str2:str) -> bool:
    cset1: List[int] = [0] * 256
    cset2: List[int] = [0] * 256
    for x in str1:
        cset1[x] = cset1[x] + 1
    for x in str2:
        cset2[x] = cset2[x] + 1
    for i in range(256):
        if (cset1[i] != cset2[i]):
            return False
    return True
```

3. URLify Given a string like 
'Mr. John Smith    '
return
'Mr.%20John%20Smith'
```C++
size_t get_num_spaces_not_at_the_end(char * gstr, size_t len, size_t & last_char_idx)
{
    size_t this_spc_count = 0;
    size_t retval = 0;
    for (size_t i = 0u; i < len; i ++)
    {
        if (gstr[i] == ' ')
        { this_spc_count ++; }
        else
        {
            retval += this_spc_count;
            this_spc_count = 0;
            last_char_idx = i;
        }
    }
    return (retval);
}

void urlify_string(char * gstr, size_t len)
{
    // Compute num_spc:= the number of spaces not at the end
    // map last valid index of original string i.e. len-1
    // to len-1 + num_spc * 2
    // set i = len -1 and 
    // set j = len-1 + num_spc * 2
    // if i is at a space, write %20 and decrement j by 3
    // else write the character and decrement j by 1
    // decrement i

    if ( len < 1 ) {return;}
    size_t last_char_idx = 0;
    size_t num_spc = get_num_spaces_not_at_the_end(gstr, len, last_char_idx);
    size_t i = (last_char_idx);
    size_t j = i + (num_spc * 2);
    if (j >= len)
    { // error condition
        return;
    }
    for ( i >= 0; i-- )
    {
        if (gstr[i] == ' ')
        {
            gstr[j-2] = '%';
            gstr[j-1] = '2';
            gstr[j] = '0';
            j = j - 3;
        }
        else
        {
            gstr[j] = gstr[i];
            j = j - 1;
        }
    }
    return;
}
```

4. palindrome permutation
```C++
bool is_perm_palindrome(const char * const gstr, size_t len)
{
    size_t char_counts[256] = {0};
    for (size_t i = 0u; i < len; i ++)
    {
        char_counts[gstr[i]] ++;
    }
    bool found_odd = true;
    for ( auto cc: char_counts )
    {
        if (cc % 2 != 0)
        {
            if (found_odd) {return (false);}
            else {found_odd = true;}
        }
        // else will be an even count. So this is not a problem
    }
    return (true);
}
```

5. One edit distance away
```C++
bool check_one_repl_away(const char * const str1, const char * const str2, size_t len1)
{
    bool found_one = false;
    for ( size_t i = 0 ; i < len1; i ++ )
    {
        if (str1[i] != str2[i])
        {
            if (found_one)
                { return (false); }
            else
                { found_one = true; }
        }
    }
    return (true);
}
bool check_one_del_away(const char * const str1, const char * const str2, size_t len1)
{
    bool found_one = false;
    size_t i = 0;
    size_t j = 0;
    for ( ; ((i < len1) && (j < (len1 - 1))); )
    {
        if (str1[i] != str2[j])
        {
            if (found_one)
                { return (false); }
            else
            { 
                found_one = true;
                i++; // only skip longer string
            }
        }
        else
        {
            i++;
            j++;
        }
    }

    return (true);
}
bool is_one_edit_away(const char * const str1, const char * const str2, size_t len1, size_t len2)
{
    if (len1 == len2) {
        return (check_one_repl_away(str1, str2, len1));
    }
    if (len1 == len2 + 1 ) {
        return (check_one_del_away(str1, str2, len1));
    }
    if (len2 == len1 + 1 ) {
        return (check_one_del_away(str2, str1, len2));
    }
}
```
6. String compression without seeing order of characters
```C++
unsigned int get_len_num(size_t num)
{
    size_t pow_ten = 1;
    for ( int i = 0; i < 8; i ++ )
    {
        if (num < pow_ten * 10)
        {
            return (i+1);
        }
        else
        {
            pow_ten = pow_ten * 10;
        }
    }
    return (9);
}
void write_char_count(char * gstr, const size_t (&char_counts)[256])
{
    size_t idx = 0;
    for (size_t i = 'a'; i <= 'Z'; i ++)
    {
        if (char_counts[i] < 1)
        { continue; }
        else
        {
            gstr[idx++] = i + 'a';
            // write string(char_counts[i]) to gstr + idx
            // increment idx
        }
    }
    gstr[idx] = '\0';
}
void compress_string_inplace(char * gstr, size_t len)
{
    size_t char_counts[256] = {0};
    for (size_t i = 0u; i < len; i ++)
    {
        if (((gstr[i] >= 'a') && (gstr[i] <= 'z')) ||
            ((gstr[i] >= 'A') && (gstr[i] <= 'Z')))
        {
            char_counts[gstr[i]] ++;
        }
    }
    comp_str_len = 0;
    for (size_t i = 'a'; i <= 'Z'; i ++)
    {
        if (char_counts[i] < 1)
        { continue; }
        else
        {
            comp_str_len += (1 + get_len_num(char_counts[i]));
        }
    }
    if (comp_str_len < len)
    {
        write_char_count(gstr, comp_str_len)
    }
}
```
6. String compression with looking at order of characters:
'aabcccccaaa' -> 'a2b1c5a3'
```python
def compress_string_inplace(gstr: str) -> str:
    last_char = ' '  #invalid
    cur_char_count = 0
    comp_str_len = 0
    len_str = len(gstr)
    ret_str = ''
    for c in gstr:
        if (c != last_char):
            # Add to comp_str_len if cur_char_count > 0
            if (cur_char_count > 0):
                # 1 for the character and len(str(cur_char_count)) for the count
                comp_str_len = comp_str_len + 1 + len(str(cur_char_count))
            # reset cur_char_count
            cur_char_count = 1
            # set last_char
            last_char = c
        else:
            cur_char_count = cur_char_count + 1
    if (cur_char_count > 0):
        # Add to comp_str_len
        # 1 for the character and len(str(cur_char_count)) for the count
        comp_str_len = comp_str_len + 1 + len(str(cur_char_count))
    if (comp_str_len < len_str):
        # build string to return
        last_char = ' '  #invalid
        cur_char_count = 0
        for c in gstr:
            if (c != last_char):
                if ( cur_char_count > 0 ):
                    ret_str = ret_str + last_char + str(cur_char_count)
                # reset cur_char_count
                cur_char_count = 1
                # set last_char
                last_char = c
            else:
                cur_char_count = cur_char_count + 1
        if (cur_char_count > 0):
            ret_str = ret_str + last_char + str(cur_char_count)
    else:
        ret_str = gstr
    return (ret_str)

```
7. Compute rotation of matrix by 90%
```python

def rotate_numpy_matrix(mat:numpy.ndarray) -> numpy.ndarray:
    '''
    Example:
    N = 2
    1 1
    0 0
    Ans:
    0 1
    0 1
    and
    N = 3
    1 1 2
    0 0 2
    0 0 2
    Ans:
    0 0 1
    0 0 1
    2 2 2
    '''
    for num_iter in range (N//2 - 1):
        for j in range(N - num_iter):
            saved_value = mat[num_iter, j]
            mat[num_iter, j] = mat[num_iter, j]
```

8. Set row and column to 0 in a matrix
```python
def set_row_col_zero(mat:List[List[int]]) -> List[List[int]]:
    row_has_zero = [False] * len(mat)
    col_has_zero = [False] * len(mat[0])
    for i,li in enumerate(mat):
        for j,_ in enumerate(li):
            if (mat[i][j] == 0):
                row_has_zero[i] = True
                col_has_zero[j] = True
    for i,li in enumerate(mat):
        for j,_ in enumerate(li):
            if (row_has_zero[i] or col_has_zero[j]):
                mat[i][j] = 0
    return (mat)
```

9. String Rotation:
```python
def is_s2_rotation_of_s1(s1:str, s2:str) -> bool:
    return (isSubstring(s2, s1+s1))
```