library ieee;
use ieee.std_logic_1164.all;

entity single_digit is
    port (C,R : in std_logic;
            output, carry : out std_logic_vector);
end single_digit;

architecture behavioral of single_digit is
begin
    process(C,R)
        variable counter : integer range 0 to 4 := 0;
    begin
        if R = '1' then
            counter := 0;
        elsif (rising_edge(C)))
            counter := counter + 1;
        end if;
        output <= counter;
    end process;
end behavioral;
