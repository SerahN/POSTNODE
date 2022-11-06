# POSTNODE

HNGi9 STAGE 2 BACKEND TASK

> This backend app takes this json format
> `{ “operation_type”: Enum <addition | subtraction | multiplication> , “x”: Integer, “y”: Integer }`,
> processes the values of x and y with respect to the operation_type,
>
> > `enum operation_type: addtion = 1, subtraction =2, multiplication = 3`
> > and returns the following json form as output
> > `{ “slackUsername”: String, "operation_type" : Enum. value, “result”: Integer }`
