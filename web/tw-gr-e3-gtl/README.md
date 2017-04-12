# PicoCTF_2017: TW_GR_E3_Gtl

**Category:** Web Exploitation
**Points:** 180
**Description:**

>Many think the third entry in the Toaster Wars: Going Rogue series didn't live up to Explorers due to its simplified gameplay, but I liked the new plot and ensemble cast better. Anyway, this [one](http://shell2017.picoctf.com:26592/) also has a flag that I can't figure out how to get...

**Hint:**

>Clearly, you can't get to the flag. But perhaps you don't need to go over to it at all?

## Write-up
There are two solutions for this challenge, one intended and the other, not so much. Firstly, I'll write about the intended solution, which is more or less considered the 100% solution.

The first solution involves no RNG and was the originally intended solution of the challenge setter. We first have to identify the couple of "bugs" in the code, particular the one with item pick up.

    // item check
    if(entity.items.length < entity.stats.maxItems){
        var itId = -1;
        var name = "";
        for(var i = 0; i < state.items.length; i++){
            if(state.items[i].location.r == entity.location.r && state.items[i].location.c == entity.location.c){
                itId = state.items[i].id;
                msg.outcome.push({
                    type: "item/get",
                    id: state.items[i].id,
                    item: state.items[i].name
                });
                break;
            }
        }
    }

    entity.items = entity.items.concat(state.items.filter(function(it){ return it.id == itId; }));
    state.items = state.items.filter(function(it){ return it.id != itId; });

Through rubber ducky debugging, you realize that at any time, items are concatenated by their IDs upon item pick up. This also means that there is no limit to the amount of items you can pick up at once, as long as the IDs are similar.

Additionally, looking into `server/config.js` reveals our flag's ID

    function createFlag(location) {
        return {
            name: "Flag",
            description: "Gives you the flag.",
            location: location,
            use: 0,
            id: 12,
            sprite: "flag",
            effects: [
                {
                    type: "revealFlag"
                }
            ]
        };
    }

This means we need to have an ID of 12 of an item to get the flag as well if we drop it. Moving to phase 2 of this solution, we need to look at another bug/feature

    socket.on("resortItems", function(){
        ...
        for(var i = 0; i < state.player.items.length; i++){
            state.player.items[i].id = i;
        ...
    })

It appears that whenever we sort items, the item's ID values are changed as well. This means, we can theoretically pick up and item, change it's ID value to `0` and drop it again. Why do that? Well, this also means it's possible to sort 13 items and have the 13th item with the same ID as the flag. However, since you can only pick up a maximum of 8 items, you need to exploit the fact you pick up all the items with the same ID value like `0`.

So, to solve this, you need to get up to level 4 with a full inventory of 8 items. Then, proceed to murder all the enemies in that level to be able to do whatever you have to do next uninterrupted. Now, proceed to drop all items except 1, sort, drop, pick up another item, sort and drop rinse and repeat till all items have an ID of 0. Then, proceed to pick them all up at once by moving over any item with ID 0. Bam, now you have more items in your inventory than you should have.

Proceed to level 5, sort and drop all your items till you are left with the 13th item. Drop the 13th item, walk back and pick it up again and you should get your flag.

The next solution was completely unintended and relies on the low ID value of flag while simultanously relying on `generator.js`.

By pure RNG, it is possible to have an item spawn in a level with an ID of 12. Using Chrome's Developers Console and repeatedly checking item values with `state.items` and `state.player.items`, it's possible to narrow it down to a single item with ID of 12. Then, resist sorting your items till you are on level 5, drop the item and pick it up again. Flag bingo!

Therefore, the flag is `the_new_feature_where_you_manage_your_own_shelf_in_the_refrigerator_was_an_interesting_addition_3a4b094d798ee2e4fc2aac44cf9a5902`.