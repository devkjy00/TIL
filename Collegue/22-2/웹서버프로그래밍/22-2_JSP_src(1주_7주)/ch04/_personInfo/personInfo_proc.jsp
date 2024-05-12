<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
	Home > Person Information
	<hr>
<%
request.setCharacterEncoding("utf-8");

String p_name = request.getParameter("p_name");
String e_code = request.getParameter("e_code");
String gender = request.getParameter("gender");
String hobby1 = request.getParameter("hobby1");
String hobby2 = request.getParameter("hobby2");
String hobby3 = request.getParameter("hobby3");

%>

	<table border=1 width=350>
		<tr>
				<th>이름(성별)</th>
				<th>사원코드</th>
				<th>취미</th>		
		</tr>
		<tr align=center>
				<td><%=p_name + "(" + gender +")" %></td>
				<td><%=e_code %></td>
				<td><%=hobby1 + "&nbsp;" + hobby2 + "&nbsp;" + hobby3 %></td>	
		</tr>
	</table>	

</body>
</html>
