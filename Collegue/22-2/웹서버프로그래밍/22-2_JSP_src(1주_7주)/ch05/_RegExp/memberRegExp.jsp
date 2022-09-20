<%@ page contentType="text/html; charset=utf-8"%>
<html>
<head>
<title>회원가입</title>
</head>
<script type="text/javascript">
	function checkMember() {
		var regExpId = /^[a-z|A-Z|ㄱ-ㅎ|ㅏ-ㅣ|가-힣]/;
		var regExpName = /^[가-힣]*$/;
		var regExpPasswd = /^[0-9]*$/;
		var regExpPhone = /^\d{3}-\d{3,4}-\d{4}$/;

		var form = document.Member;

		var id = form.id.value;
		var name = form.name.value;
		var passwd = form.passwd.value;
		var phone = form.phone1.value + "-" + form.phone2.value + "-" + form.phone3.value;

		if (!regExpId.test(id)) {
			alert("아이디는 문자로 시작해 주세요!");
			form.id.select();
			return;
		}
		if (!regExpName.test(name)) {
			alert("이름은 한글만으로 입력해 주세요!");
			return;
		}
		if (!regExpPasswd.test(passwd)) {
			alert("비밀번호는 숫자만으로 입력해 주세요!");
			return;
		}
		if (!regExpPhone.test(phone)) {
			alert("연락처 입력을 확인해 주세요!");
			return;
		}
		form.submit();
	}
</script>
<body>
	<h3>회원 가입</h3>
	<form action="memberRegExp_proc.jsp" name="Member" method="post">
	<fieldset style="width:300px">
		<legend>개인 정보 입력</legend>
		아이디 : <br> <input type="text" name="id">
		<p>	비밀번호 : <br> <input type="password" name="passwd">
		<p>	이름 : <br> <input type="text" name="name">
		<p>	연락처 : <br> <select name="phone1">
				<option value="010">010</option>
				<option value="011">011</option>
				<option value="016">016</option>
				<option value="017">017</option>
				<option value="019">019</option>
			</select> - <input type="text" maxlength="4" size="4" name="phone2"> -
			<input type="text" maxlength="4" size="4" name="phone3">
		<p>	<input type="button" value="가입하기" onclick="checkMember()"> 
	</fieldset>
	</form>
</body>
</html>