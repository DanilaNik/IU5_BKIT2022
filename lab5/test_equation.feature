Feature: 
    Scenario Outline
    This app solve biquatratic equation

    Scenario Outline: Solve the equation with correct value
        Given The A coefficient <A>
        And The B coefficient <B>
        And The C coefficient <C>
        When Solve the equation
        Then I get <D> roots

        Examples:
        |A |   B|   C|D|

        | 1|  12|  36|0|
        | 6|  60|  54|0|
        | 3|  31|  56|0|

        | 1|   1|   0|1|
        | 5|  15|   0|1|
        |30|  18|   0|1|

        | 3|  -5| -28|2|
        | 3| -14|-117|2|
        |11| -86|-117|2|

        | 1|  -9|   0|3|
        | 3| -75|   0|3|
        | 7|-112|   0|3|

        | 7|-287|2800|4|
        |13|-689|2548|4|
        | 1| -73| 576|4|