# PicoCTF_2017: Forest

**Category:** Reverse Engineering
**Points:** 200
**Description:**

>I was wandering the [forest](forest) and found a file. It came with some [string](string.txt)

**Hint:**

>A number of disassemblers have tools to help view structs

## Write-up
This challenge was a fun one, given that it had a varying level of requirements in it. For the most part, IDA Pro will be very useful but for us freebies out there, we can use [RetDec](https://retdec.com/decompilation). We get a [file decompiled like this](forest.c).

This is an example of binary tree sorting, with each letter sorted with the smaller character going to the left and the larger character going to the right. The string we have to sort in this case is `yuoteavpxqgrlsdhwfjkzi_cmbn`.

Next, the string we are given refers to the ways we should select characters. `L` means go down the left branch, `R` goes down the right branch while `D` means this character. If we compare the string we got and the [top-down tree we graphed](images/graph.jpg), we get the flag.

Therefore, the flag is `you_could_see_the_forest_for_the_trees_ckyljfxyfmsw`.