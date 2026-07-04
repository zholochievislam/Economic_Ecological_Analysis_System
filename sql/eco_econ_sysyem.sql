use eco_econ_system;

insert into Ecologic_Indicator (EcologicID, Name, Unit) values
(1,"CO2_Emissions", "T"),
(2,"Safe_water_access", "%"),
(3,"Forest_loss_fire", "ha");
 insert into Economic_indicator (EconomicID, Name, Unit) values
 (1,"GDP_per_capita", "$"),
 (2,"Inflation_rate", "%"),
 (3,"Population", "people");
 
ALTER TABLE Econ_Data
MODIFY COLUMN Value DECIMAL(20,4);
 
 select * from Country;