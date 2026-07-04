-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema eco_econ_system
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema eco_econ_system
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `eco_econ_system` DEFAULT CHARACTER SET utf8 ;
USE `eco_econ_system` ;

-- -----------------------------------------------------
-- Table `eco_econ_system`.`Country`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eco_econ_system`.`Country` (
  `CountryID` INT NOT NULL AUTO_INCREMENT,
  `CountryName` VARCHAR(100) NOT NULL,
  `Code` VARCHAR(3) NOT NULL,
  `Region` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`CountryID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `eco_econ_system`.`Economic_Indicator`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eco_econ_system`.`Economic_Indicator` (
  `EconomicID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(100) NOT NULL,
  `Unit` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`EconomicID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `eco_econ_system`.`Ecologic_Indicator`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eco_econ_system`.`Ecologic_Indicator` (
  `EcologicID` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(100) NOT NULL,
  `Unit` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`EcologicID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `eco_econ_system`.`Econ_Data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eco_econ_system`.`Econ_Data` (
  `EconDataID` VARCHAR(200) NOT NULL,
  `Year` VARCHAR(100) NOT NULL,
  `Value` VARCHAR(100) NOT NULL,
  `Economic_Indicator_EconomicID` INT NOT NULL,
  `Country_CountryID` INT NOT NULL,
  PRIMARY KEY (`EconDataID`),
  INDEX `fk_Econ_Data_Economic_Indicator1_idx` (`Economic_Indicator_EconomicID` ASC) VISIBLE,
  INDEX `fk_Econ_Data_Country1_idx` (`Country_CountryID` ASC) VISIBLE,
  CONSTRAINT `fk_Econ_Data_Economic_Indicator1`
    FOREIGN KEY (`Economic_Indicator_EconomicID`)
    REFERENCES `eco_econ_system`.`Economic_Indicator` (`EconomicID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Econ_Data_Country1`
    FOREIGN KEY (`Country_CountryID`)
    REFERENCES `eco_econ_system`.`Country` (`CountryID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `eco_econ_system`.`Ecol_Data`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `eco_econ_system`.`Ecol_Data` (
  `EcolDataID` VARCHAR(200) NOT NULL,
  `Year` VARCHAR(100) NOT NULL,
  `Value` VARCHAR(100) NOT NULL,
  `Ecologic_Indicator_EcologicID` INT NOT NULL,
  `Country_CountryID` INT NOT NULL,
  PRIMARY KEY (`EcolDataID`),
  INDEX `fk_Ecol_Data_Ecologic_Indicator1_idx` (`Ecologic_Indicator_EcologicID` ASC) VISIBLE,
  INDEX `fk_Ecol_Data_Country1_idx` (`Country_CountryID` ASC) VISIBLE,
  CONSTRAINT `fk_Ecol_Data_Ecologic_Indicator1`
    FOREIGN KEY (`Ecologic_Indicator_EcologicID`)
    REFERENCES `eco_econ_system`.`Ecologic_Indicator` (`EcologicID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_Ecol_Data_Country1`
    FOREIGN KEY (`Country_CountryID`)
    REFERENCES `eco_econ_system`.`Country` (`CountryID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
