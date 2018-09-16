<?php 

    error_reporting(E_ALL); 
    ini_set('display_errors',1); 

    include('dbcon.php');
        

    $stmt = $con->prepare('select * from qr_data');
    $stmt->execute();

    if ($stmt->rowCount() > 0)
    {
        $data = array(); 

        while($row=$stmt->fetch(PDO::FETCH_ASSOC))
        {
            extract($row);
    
            
            array_push($data, 
                array('Id'=>$id,
                'Name'=>$Name,
                'Date_limit'=>$Date_limit,
                'Date_enter'=>$Date_enter,
                'Company'=>$Company,
                'Weight'=>$Weight,
                //'country'=>$country
            ));
        }

        header("Content-Type:application/json;charset=utf8");
        $json = json_encode(array("qr_data"=>$data), JSON_PRETTY_PRINT+JSON_UNESCAPED_UNICODE);
        echo $json;
    }

?>
