
sub senyang{
			if(open(IN,"./charalog/main/$cnum\.cgi")){
			@E_DATA = <IN>;
			close(IN);
			($eid,$epass,$ename,$echara,$estr,$eint,$elea,$echa,$esol,$egat,$econ,$egold,$erice,$ecex,$eclass,$earm,$ebook,$ebank,$esub1,$esub2,$epos,$emes,$ehost,$edate,$email,$eos,$eskill,$epoint,$ect,$elevel,$eexp,$ecodea,$ecodeb,$eqpoint) = split(/<>/,$E_DATA[0]);
			if($econ eq $kcon){
			open(IN,"$COUNTRY_LIST") or &ERR2('������ ���� �ʾҽ��ϴ�. err no :country');
			@COU_DATA = <IN>;
			close(IN);
			for($i=0;$i<@COU_DATA;$i++){
			($xvcid,$xvname,$xvele,$xvmark,$xvking,$xvmes,$xvsub,$xvpri) = split(/<>/,$COU_DATA[$i]);
			if($xvcid eq $kcon){
			splice(@COU_DATA,$i,1,"$xvcid<>$xvname<>$xvele<>$xvmark<>$eid<>$xvmes<>$xvsub<>$xvpri<>\n");
			last;
								}
							}
							&MAP_LOG2("<font color=red>[���]</font>$xvname���� ���ⱺ�ַ� $ename���� �����Ǿ����ϴ�.");
							&MAP_LOG("<font color=red>[���]</font>$xvname���� ���ⱺ�ַ� $ename���� �����Ǿ����ϴ�.");
							&K_LOG("$ename���� �ձ��� �����Ͽ����ϴ�.");
							$cou_king[$kcon] = $eid;
							$kclass = int($kclass*3/4);
						}else{
							&K_LOG("$ename���� �Ʊ��� ����� �ƴմϴ�.");
						}

					}else{
						&K_LOG("���簡���� ��밡 �����ϴ�.");
					}	
}
1;

