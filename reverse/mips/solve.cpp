#include <iostream>
#include <limits.h>
#include <stdio.h>

int reg[32] = {};

void run(int i) {
    L0:
        // printf("Entering L0\r");
        // li      $v0, 5
        // syscall
        reg[4]  = i;                            // move    $4, $v0         # $4 holds our input
        // addiu   $sp, $sp, -32
        // sw      $31, 28($sp)
        // sw      $16, 24($sp)
        reg[6]  = -16777216;                    // li      $6, -16777216   # Load -16777216 into $6
        reg[6]  = reg[4] & reg[6];              // and     $6, $4, $6      # $6 = $4 & $6
        reg[16] = 16711680;                     // li      $16, 16711680   # Load 16711680 into $16
        reg[16] = reg[4] & reg[16];             // and     $16, $4, $16    # $16 = $4 & $16
        reg[7]  = reg[4] & 0xff00;              // andi    $7, $4, 0xff00  # $7 = $4 & 0xff00
        reg[4]  = reg[4] & 0xff;                // andi    $4, $4, 0xff    # $4 = $4 & 0xff // 0?
        reg[3]  = reg[6] >> 24;                 // sra     $3, $6, 24
        reg[2]  = 0;                            // move    $2, $0          # Move 0 into $2

    L3:
        // printf("Entering L3\r");
        reg[5]  = (reg[2] < 13);                // slt     $5, $2, 13      # If $2 >= 13
        reg[2]  = reg[2] + 1;                   // addiu   $2, $2, 1       # $2 = $2 + 1
        if (reg[5] == 0) { goto L2; }           // beq     $5, $0, $L2     # Branch to L2
        reg[3]  = reg[3] - 13;                  // addiu   $3, $3, -13
        goto L3;                                // b       $L3

    L2:
        // printf("Entering L2\r");
        reg[3]  = reg[3] - 6;                   // addiu   $3, $3, -6      # $3 = $3 - 6
        reg[5]  = reg[3] << 24;                 // sll     $5, $3, 24
        reg[16] = reg[16] >> 16;                // sra     $16, $16, 16
        reg[2]  = reg[16] - 81;                 // addiu   $2, $16, -81    # $2 = $16 - 81
        reg[8]  = reg[2] << 6;                  // sll     $8, $2, 6
        reg[3]  = reg[2] << 8;                  // sll     $3, $2, 8
        reg[3]  = reg[3] - reg[8];              // subu    $3, $3, $8      # $3 = $3 - $8
        reg[3]  = reg[2] - reg[3];              // subu    $3, $2, $3      # $3 = $2 - $3
        reg[7]  = reg[7] >> 8;                  // sra     $7, $7, 8
        reg[2]  = reg[4] << 1;                  // sll     $2, $4, 1
        reg[2]  = reg[2] + 3;                   // addiu   $2, $2, 3       # $2 = $2 + 3
        reg[3]  = reg[3] << 16;                 // sll     $3, $3, 16
        if (reg[7] != reg[2]) { goto L7; }      // bne     $7, $2, $L7     # If $7 != $2, branch to L7
        reg[2] = 94;                            // li      $2, 94
        goto L4;                                // b       $L4             # Branch to $L4

    L7:
        // printf("Entering L7\r");
        reg[2]  = 165;                          // li      $2, 165

    L4:
        // printf("Entering L4\r");
        reg[2]  = reg[2] - 94;                  // addiu   $2, $2, -94     # $2 = $2 - 94
        reg[2]  = reg[2] << 8;                  // sll     $2, $2, 8
        reg[6]  = unsigned(reg[6]) >> 24;       // srl     $6, $6, 24
        reg[16] = reg[6] - reg[16];             // subu    $16, $6, $16    # $16 = $6 - $16
        reg[4]  = reg[4] - reg[16];             // subu    $4, $4, $16     # $4 = $4 - $16
        reg[3]  = reg[5] + reg[3];              // addu    $3, $5, $3      # $3 = $5 + $3
        reg[3]  = reg[2] + reg[3];              // addu    $3, $2, $3      # $3 = $2 + $3
        reg[16] = reg[4] + reg[3];              // addu    $16, $4, $3     # $16 = $4 + $3
        if (reg[16] != 0) { goto L5; }          // bne     $16, $0, $L5    # If $16 != 0, branch to L5
        // li      $v0, 4
        // la      $a0, success
        // syscall
        // lw      $28, 16($sp)
        reg[2]  = 16;                           // move    $2, $16
        goto L9;

    L5:
    L9:
        {};
}

int main() {
    for (int i = INT_MIN; i < INT_MAX; i++) {
        run(i);

        if (i % 16777216 == 0) {
            printf("Trying %d, received %d\n", i, reg[16]); 
        }

        if (reg[16] == 0) {
            printf("Found our flag: %d\n", i);
            break;
        }

        // Clearing registers
        for (int i = 0; i < sizeof(reg)/sizeof(int); i++) {
            reg[i] = 0;
        }
    }
}