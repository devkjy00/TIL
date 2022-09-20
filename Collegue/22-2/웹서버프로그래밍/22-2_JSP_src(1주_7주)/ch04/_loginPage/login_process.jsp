<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>로그인 정보</title>
</head>
<body>
	Home > Login > Information
	<hr>
	<%
	request.setCharacterEncoding("utf-8");  //문자 인코딩 설정
		
	String id = request.getParameter("id");
	String passwd = request.getParameter("passwd");
	%>
	
	<table border=1>
		<tr>
				<th>아이디</th>
				<th>비밀번호</th>	
		</tr>
		<tr>
				<td><%= id %></td>
				<td><%= passwd %></td>	
		</tr>
	</table>	
</body>
</html>