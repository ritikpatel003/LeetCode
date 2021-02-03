class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        p=0
        bull=0
        cow=0
        secret=list(secret)
        guess=list(guess)
        for i in guess:
            if i == secret[p]:
                bull+=1
                secret[p]="x"
                guess[p]="y"
            p+=1
        for i in guess:
            if i in secret:
                secret[secret.index(i)]="x"
                cow+=1
        return str(bull)+"A"+str(cow)+"B"