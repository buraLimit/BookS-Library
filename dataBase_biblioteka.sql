-- phpMyAdmin SQL Dump
-- version 4.9.2
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 14, 2021 at 11:30 AM
-- Server version: 10.4.11-MariaDB
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `biblioteka`
--

DELIMITER $$
--
-- Procedures
--
CREATE DEFINER=`root`@`localhost` PROCEDURE `pro_dodajAutora` (IN `autorU` TEXT, OUT `text` TEXT)  NO SQL
BEGIN

DECLARE broj int DEFAULT 0;

SELECT COUNT(*) 

INTO broj

FROM autor WHERE autor.naziv_aut = autorU;

IF broj>0 THEN

set text='Autor vec postoji';

ELSE

INSERT INTO autor (autor.naziv_aut)

VALUES(autorU);

set text='Autor uspesno dodat!';

END if;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pro_dodajIzdavaca` (IN `nazivU` TEXT, IN `gradU` TEXT, IN `adresaU` TEXT, OUT `text1` TEXT)  BEGIN
DECLARE broj int DEFAULT 0;
SELECT COUNT(*) 
INTO broj
FROM izdavac WHERE izdavac.ime_izdavaca = nazivU;
IF broj>0 THEN
set text1='Izdavac vec postoji!';
elseif (nazivU = '' or gradU= '' or adresaU= '') then
set text1='Polja ne mogu biti prazna';
ELSE
INSERT INTO izdavac (izdavac.ime_izdavaca,izdavac.grad, izdavac.adresa_izdavaca)
VALUES(nazivU,gradU,adresaU);
set text1='Izdavac uspesno dodat!';
END if;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pro_dodajKategoriju` (IN `kategorijaU` TEXT, OUT `text1` TEXT)  BEGIN
DECLARE broj int DEFAULT 0;
SELECT COUNT(*) 
INTO broj
FROM kategorija WHERE kategorija.naziv_kat = kategorijaU;
IF broj>0 THEN
set text1='Kategorija vec postoji!';
ELSE
INSERT INTO kategorija (kategorija.naziv_kat)
VALUES(kategorijaU);
set text1='Kategorija uspesno dodata!';
END if;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pro_dodajKnjigu` (IN `naslovU` TEXT, IN `autorU` TEXT, IN `izdanjeU` INT, IN `godinaU` INT, IN `isbnU` TEXT, IN `kategorijaU` TEXT, IN `izdavacU` TEXT, IN `kolicinaU` INT, OUT `text` TEXT)  NO SQL
BEGIN
DECLARE nova int DEFAULT 0;
if (naslovU = '' or autorU='' OR izdanjeU='' OR godinaU='' or isbnU='' or kategorijaU='' OR izdavacU='' OR kolicinaU='')

then select 'Sva polja morate popuniti';

ELSE

INSERT into knjiga (knjiga.naslov,knjiga.id_autora,knjiga.izdanje,knjiga.godina,knjiga.ISBN,knjiga.id_kategorije, knjiga.id_izdavaca, knjiga.kolicina)

VALUES (naslovU, (SELECT autor.id_autora from autor WHERE autor.naziv_aut=autorU),

      izdanjeU, godinaU,isbnU, 

       (SELECT kategorija.id_kategorije from kategorija WHERE kategorija.naziv_kat = kategorijaU), 

       (SELECT izdavac.id_izdavaca FROM izdavac WHERE izdavac.ime_izdavaca=izdavacU), kolicinaU);

END if;



END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pro_izdajKnjigu` (IN `korisnikID` INT, IN `knjigaID` INT, OUT `text` TEXT)  NO SQL
BEGIN
DECLARE broj int DEFAULT 0;
SELECT COUNT(*) 
INTO broj
FROM primerak WHERE primerak.id_primerka = knjigaID AND slobodna = 'Ne';
IF broj>0 THEN
set text='Knjiga je vec izdata';
ELSE
INSERT INTO izdata_knjiga (izdata_knjiga.id_primerka,izdata_knjiga.id_korisnika, dat_uzimanja)
VALUES(knjigaID, korisnikID, NOW());
set text='Knjiga izdata';
END if;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pro_obiriKorisnika` (IN `ID` INT, OUT `text1` TEXT)  BEGIN
DECLARE broj int DEFAULT 0;
SELECT COUNT(*) 
INTO broj
FROM izdata_knjiga WHERE izdata_knjiga.id_korisnika = ID;
IF broj>0 THEN
set text1='Ne mozete obrisati clana jer nije vratio knjigu!';
ELSE
delete from korisnik 
WHERE korisnik.id_korisnika = ID;
set text1='Korisnik obrisan';
END if;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pro_obrisiKorisnika` (IN `ID` INT, OUT `text1` TEXT)  BEGIN
DECLARE broj int DEFAULT 0;
SELECT COUNT(*) 
INTO broj
FROM izdata_knjiga WHERE izdata_knjiga.id_korisnika = ID;
IF broj>0 THEN
set text1='Ne mozete obrisati clana jer nije vratio knjigu!';
ELSE
delete from korisnik 
WHERE korisnik.id_korisnika = ID;
set text1='Korisnik obrisan';
END if;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pro_unesiKorisnika` (IN `imeU` VARCHAR(20), IN `prezimeU` VARCHAR(20), IN `adresaU` TEXT, IN `brojtelU` VARCHAR(14), IN `emailU` TEXT)  NO SQL
BEGIN

if (imeU='' or prezimeU ='' or adresaU ='' or brojtelU ='')

then select 'Nema upisivanja, fali nesto';

else

INSERT INTO korisnik (korisnik.ime,korisnik.prezime,korisnik.adresa,korisnik.broj_tel,korisnik.email)

VALUES (imeU, prezimeU, adresaU, brojtelU ,emailU);

end if;

END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pro_updateKorisnik` (IN `idU` INT, IN `imeU` TEXT, IN `prezimeU` TEXT, IN `adresaU` TEXT, IN `brojtelU` TEXT, IN `emailU` TEXT)  BEGIN
if (imeU='' or prezimeU ='' or adresaU ='' or brojtelU ='' )
then select 'Nema upisivanja, fali nesto';
else
update korisnik 
set korisnik.ime = imeU,korisnik.prezime = prezimeU,korisnik.adresa = adresaU,korisnik.broj_tel=brojtelU,korisnik.email=emailU
where korisnik.id_korisnika=idU;
end if;
END$$

CREATE DEFINER=`root`@`localhost` PROCEDURE `pro_vratiKnjigu` (IN `korisnikID` INT, IN `knjigaID` INT, OUT `text` TEXT)  NO SQL
BEGIN
DECLARE broj int DEFAULT 0;
SELECT COUNT(*) 
INTO broj
FROM izdata_knjiga WHERE izdata_knjiga.id_primerka = knjigaID AND izdata_knjiga.id_korisnika = korisnikID;
IF broj=0 THEN
set text='Pogresne vrednosti';
ELSE
delete from izdata_knjiga 
WHERE izdata_knjiga.id_primerka = knjigaID AND izdata_knjiga.id_korisnika = korisnikID;
set text='Knjiga vracena';
END if;
END$$

DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `autor`
--

CREATE TABLE `autor` (
  `id_autora` int(11) NOT NULL,
  `naziv_aut` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `autor`
--

INSERT INTO `autor` (`id_autora`, `naziv_aut`) VALUES
(2, 'Stephen King'),
(3, 'Svetislav Basara'),
(4, 'Hans Rosling'),
(5, 'Fredrik Bakman'),
(6, 'Las Kepler'),
(10, 'autor'),
(11, 'Miroslav Miskovic');

-- --------------------------------------------------------

--
-- Table structure for table `izdata_knjiga`
--

CREATE TABLE `izdata_knjiga` (
  `id_korisnika` int(11) NOT NULL,
  `id_primerka` int(11) NOT NULL,
  `dat_uzimanja` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `izdata_knjiga`
--

INSERT INTO `izdata_knjiga` (`id_korisnika`, `id_primerka`, `dat_uzimanja`) VALUES
(2, 1, '2021-09-14'),
(2, 6, '2021-10-13');

--
-- Triggers `izdata_knjiga`
--
DELIMITER $$
CREATE TRIGGER `trig_izataKnjiga` AFTER INSERT ON `izdata_knjiga` FOR EACH ROW Begin 
declare izdata int;
select new.id_primerka into izdata;

update primerak
set slobodna= 'Ne' 
where primerak.id_primerka = izdata; 
END
$$
DELIMITER ;
DELIMITER $$
CREATE TRIGGER `trig_vracenaKnjiga` AFTER DELETE ON `izdata_knjiga` FOR EACH ROW Begin 
declare vracena int;
select old.id_primerka into vracena;

update primerak
set slobodna= 'Da' 
where primerak.id_primerka = vracena; 
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `izdavac`
--

CREATE TABLE `izdavac` (
  `id_izdavaca` int(11) NOT NULL,
  `ime_izdavaca` text NOT NULL,
  `grad` text NOT NULL,
  `adresa_izdavaca` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `izdavac`
--

INSERT INTO `izdavac` (`id_izdavaca`, `ime_izdavaca`, `grad`, `adresa_izdavaca`) VALUES
(1, 'Laguna', 'Beograd', 'Kralja Petra 45'),
(2, 'Vulkan', 'Beograd', 'Pariska 20'),
(3, 'Booka', 'Beograd', 'Cara Lazara 12'),
(7, 'izdavac', 'a', 'a');

-- --------------------------------------------------------

--
-- Table structure for table `kategorija`
--

CREATE TABLE `kategorija` (
  `id_kategorije` int(11) NOT NULL,
  `naziv_kat` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `kategorija`
--

INSERT INTO `kategorija` (`id_kategorije`, `naziv_kat`) VALUES
(1, 'fikcija'),
(2, 'roman'),
(3, 'nauka'),
(4, 'triler'),
(6, 'psihologija'),
(23, 'kategorija');

-- --------------------------------------------------------

--
-- Table structure for table `knjiga`
--

CREATE TABLE `knjiga` (
  `id_knjige` int(11) NOT NULL,
  `naslov` text NOT NULL,
  `id_autora` int(11) NOT NULL,
  `izdanje` int(11) NOT NULL,
  `godina` int(11) NOT NULL,
  `ISBN` text NOT NULL,
  `id_kategorije` int(11) NOT NULL,
  `id_izdavaca` int(11) NOT NULL,
  `kolicina` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `knjiga`
--

INSERT INTO `knjiga` (`id_knjige`, `naslov`, `id_autora`, `izdanje`, `godina`, `ISBN`, `id_kategorije`, `id_izdavaca`, `kolicina`) VALUES
(1, 'Salemovo', 2, 6, 2018, '12356895663', 1, 1, 5),
(3, 'TO', 2, 2, 2018, '85621456121', 1, 1, 2),
(6, 'Mein Kampf', 3, 1, 2016, '84562845621', 2, 2, 1),
(7, 'Uznemireni ljudi', 5, 1, 2020, '9789021406428', 2, 1, 3),
(15, 'Covek po imenu Uve', 5, 1, 2015, '9781476738024', 2, 1, 2),
(64, 'Hipnotizer', 6, 2, 2011, '9780007429561', 1, 2, 2),
(65, 'Senka', 6, 3, 2019, '9788610028478', 4, 1, 2),
(82, 'Knjiga', 5, 1, 1, '1', 3, 3, 1);

--
-- Triggers `knjiga`
--
DELIMITER $$
CREATE TRIGGER `trigger_dodajPrimerke` AFTER INSERT ON `knjiga` FOR EACH ROW BEGIN
DECLARE komadi int;
declare maximum int;
set komadi = 0;
select new.kolicina into maximum;
while komadi < maximum
		DO
        INSERT into primerak(primerak.id_knjige)
        VALUES( (select NEW.id_knjige));
        set komadi = komadi + 1;
end WHILE;
END
$$
DELIMITER ;

-- --------------------------------------------------------

--
-- Table structure for table `korisnik`
--

CREATE TABLE `korisnik` (
  `id_korisnika` int(11) NOT NULL,
  `ime` varchar(20) NOT NULL,
  `prezime` varchar(20) NOT NULL,
  `adresa` text NOT NULL,
  `broj_tel` varchar(14) NOT NULL,
  `email` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `korisnik`
--

INSERT INTO `korisnik` (`id_korisnika`, `ime`, `prezime`, `adresa`, `broj_tel`, `email`) VALUES
(1, 'Marko', 'Markovic', 'Kralja Milutina 11', '3816626698762', 'marko@yahoo.com'),
(2, 'Dusan', 'Zdravkovic', 'Milentija Popovica 99', '+381639875632', ''),
(18, 'Marko', 'Markovic', 'Visnjicka 1a', '3816698875', 'markoоооо@gmail.com');

-- --------------------------------------------------------

--
-- Table structure for table `primerak`
--

CREATE TABLE `primerak` (
  `id_primerka` int(11) NOT NULL,
  `slobodna` text NOT NULL DEFAULT 'Da',
  `id_knjige` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `primerak`
--

INSERT INTO `primerak` (`id_primerka`, `slobodna`, `id_knjige`) VALUES
(1, 'Ne', 15),
(6, 'Ne', 7),
(7, 'Da', 7),
(8, 'Da', 7),
(10, 'Da', 15),
(11, 'Da', 6),
(12, 'Da', 3),
(13, 'Da', 3),
(14, 'Da', 1),
(15, 'Da', 1),
(16, 'Da', 1),
(17, 'Da', 1),
(18, 'Da', 1),
(19, 'Da', 64),
(20, 'Da', 64),
(23, 'Da', 65),
(24, 'Da', 65),
(54, 'Da', 82);

-- --------------------------------------------------------

--
-- Stand-in structure for view `view_prikazknjiga`
-- (See below for the actual view)
--
CREATE TABLE `view_prikazknjiga` (
`id_knjige` int(11)
,`naslov` text
,`naziv_aut` varchar(50)
,`izdanje` int(11)
,`godina` int(11)
,`ISBN` text
,`naziv_kat` varchar(20)
,`ime_izdavaca` text
,`kolicina` int(11)
,`Slobodne` bigint(21)
);

-- --------------------------------------------------------

--
-- Structure for view `view_prikazknjiga`
--
DROP TABLE IF EXISTS `view_prikazknjiga`;

CREATE ALGORITHM=UNDEFINED DEFINER=`root`@`localhost` SQL SECURITY DEFINER VIEW `view_prikazknjiga`  AS  select `knjiga`.`id_knjige` AS `id_knjige`,`knjiga`.`naslov` AS `naslov`,`autor`.`naziv_aut` AS `naziv_aut`,`knjiga`.`izdanje` AS `izdanje`,`knjiga`.`godina` AS `godina`,`knjiga`.`ISBN` AS `ISBN`,`kategorija`.`naziv_kat` AS `naziv_kat`,`izdavac`.`ime_izdavaca` AS `ime_izdavaca`,`knjiga`.`kolicina` AS `kolicina`,count(`primerak`.`slobodna`) AS `Slobodne` from ((((`knjiga` left join `autor` on(`knjiga`.`id_autora` = `autor`.`id_autora`)) left join `kategorija` on(`knjiga`.`id_kategorije` = `kategorija`.`id_kategorije`)) left join `izdavac` on(`knjiga`.`id_izdavaca` = `izdavac`.`id_izdavaca`)) left join `primerak` on(`knjiga`.`id_knjige` = `primerak`.`id_knjige`)) where `primerak`.`slobodna` = 'Da' group by `primerak`.`id_knjige` ;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `autor`
--
ALTER TABLE `autor`
  ADD PRIMARY KEY (`id_autora`);

--
-- Indexes for table `izdata_knjiga`
--
ALTER TABLE `izdata_knjiga`
  ADD UNIQUE KEY `id_primerka` (`id_primerka`) USING BTREE,
  ADD KEY `id_korisnika` (`id_korisnika`);

--
-- Indexes for table `izdavac`
--
ALTER TABLE `izdavac`
  ADD PRIMARY KEY (`id_izdavaca`);

--
-- Indexes for table `kategorija`
--
ALTER TABLE `kategorija`
  ADD PRIMARY KEY (`id_kategorije`);

--
-- Indexes for table `knjiga`
--
ALTER TABLE `knjiga`
  ADD PRIMARY KEY (`id_knjige`),
  ADD KEY `id_kategorije` (`id_kategorije`),
  ADD KEY `id_autora` (`id_autora`),
  ADD KEY `id_izdavaca` (`id_izdavaca`);

--
-- Indexes for table `korisnik`
--
ALTER TABLE `korisnik`
  ADD PRIMARY KEY (`id_korisnika`);

--
-- Indexes for table `primerak`
--
ALTER TABLE `primerak`
  ADD PRIMARY KEY (`id_primerka`),
  ADD KEY `id_knjige` (`id_knjige`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `autor`
--
ALTER TABLE `autor`
  MODIFY `id_autora` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT for table `izdavac`
--
ALTER TABLE `izdavac`
  MODIFY `id_izdavaca` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `kategorija`
--
ALTER TABLE `kategorija`
  MODIFY `id_kategorije` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `knjiga`
--
ALTER TABLE `knjiga`
  MODIFY `id_knjige` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- AUTO_INCREMENT for table `korisnik`
--
ALTER TABLE `korisnik`
  MODIFY `id_korisnika` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT for table `primerak`
--
ALTER TABLE `primerak`
  MODIFY `id_primerka` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=55;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `izdata_knjiga`
--
ALTER TABLE `izdata_knjiga`
  ADD CONSTRAINT `izdata_knjiga_ibfk_1` FOREIGN KEY (`id_primerka`) REFERENCES `primerak` (`id_primerka`),
  ADD CONSTRAINT `izdata_knjiga_ibfk_2` FOREIGN KEY (`id_korisnika`) REFERENCES `korisnik` (`id_korisnika`);

--
-- Constraints for table `knjiga`
--
ALTER TABLE `knjiga`
  ADD CONSTRAINT `knjiga_ibfk_1` FOREIGN KEY (`id_kategorije`) REFERENCES `kategorija` (`id_kategorije`),
  ADD CONSTRAINT `knjiga_ibfk_2` FOREIGN KEY (`id_autora`) REFERENCES `autor` (`id_autora`),
  ADD CONSTRAINT `knjiga_ibfk_3` FOREIGN KEY (`id_izdavaca`) REFERENCES `izdavac` (`id_izdavaca`);

--
-- Constraints for table `primerak`
--
ALTER TABLE `primerak`
  ADD CONSTRAINT `primerak_ibfk_1` FOREIGN KEY (`id_knjige`) REFERENCES `knjiga` (`id_knjige`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
