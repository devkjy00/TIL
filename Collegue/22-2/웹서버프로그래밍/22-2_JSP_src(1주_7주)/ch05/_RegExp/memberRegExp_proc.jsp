<%@ page contentType="text/html; charset=utf-8"%>
<html>
<head>
<title>회원 가입</title>
</head>
<body>
	<%
		request.setCharacterEncoding("UTF-8");
	%>
	<p>	아이디 : <%=request.getParameter("id")%>
	<p>	비밀번호 :	<%=request.getParameter("passwd")%>
	<p>	이름 : <%=request.getParameter("name")%>
	<p>	연락처 : <%=request.getParameter("phone1")%>-<%=request.getParameter("phone2")%>-<%=request.getParameter("phone3")%>
</body>
</html>