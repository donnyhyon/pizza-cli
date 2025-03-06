# pizza-cli
CLI tool to calculate pizza dough ingredients.
Variables:
- size of balls
- number of balls
- hydration
- preferment
    - biga
    - poolish

### To Run
1. Add repo folder to user environment variables PATH.

### Commands
```
pizza -h
pizza -b 100 # 100% biga 
pizza -p 30 # 30% poolish
pizza -r 75 # 75% hydration- no prefermend
pizza -b 100 -r 65 # 100% biga, 65% hydration
```

### TODO
- add warning when poolish water > total water.
- tests
