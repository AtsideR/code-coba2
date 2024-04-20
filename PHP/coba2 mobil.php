<?php
Class MobilSport{
    private $merek;
    private $nama;
    private $tahun;
    private $hp;

    public function __construct($tahun, $merek, $nama, $hp)
    {
        $this->tahun = $tahun;
        $this->merek = $merek;
        $this->nama = $nama;
        $this->hp = $hp;       
    }

    public function settahun($tahunbaru){
        $this->tahun = $tahunbaru;
    }

    public function setnama($namabaru){
        $this->nama = $namabaru;
    }

    public function sethp($hpbaru){
        $this->hp = $hpbaru;
    }

    public function gettahun(){
        return $this->tahun;
    }

    public function getmerek(){
        return $this->merek;
    }

    public function getnama(){
        return $this->nama;
    }

    public function gethp(){
        return $this->hp;
    }
}

$ngeng_ngeng = new MobilSport("2015", "Koenigsegg", "Agera RS", "960 hp");
echo"Mobil - Mobil Sport<br>";
echo"---tahun " . $ngeng_ngeng->gettahun() . "---<br>";
echo $ngeng_ngeng->getmerek() . "<br>";
echo $ngeng_ngeng->getnama() . "<br>";
echo $ngeng_ngeng->gethp() . "<br>";
echo "<br>";

$ngeng_ngeng->settahun("2021");
$ngeng_ngeng->setnama("Jesko Absolut");
$ngeng_ngeng->sethp("1280");

echo"---tahun " . $ngeng_ngeng->gettahun() . "---<br>";
echo $ngeng_ngeng->getmerek() . "<br>";
echo $ngeng_ngeng->getnama() . "<br>";
echo $ngeng_ngeng->gethp() . "<br>";
echo "<br>";

$ngeng_ngeng->settahun("2024");
$ngeng_ngeng->setnama("Gemera");
$ngeng_ngeng->sethp("2300");

echo"---tahun " . $ngeng_ngeng->gettahun() . "---<br>";
echo $ngeng_ngeng->getmerek() . "<br>";
echo $ngeng_ngeng->getnama() . "<br>";
echo $ngeng_ngeng->gethp() . "<br>";
echo "<br>";
?>