<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	request.setCharacterEncoding("UTF-8");
	String siteName = request.getParameter("siteName");
%>
<html>
<body>
<h3>>> IncludeParam_proc.jsp</h3>
html 문서에서 전달된 siteName은 
<b><%=siteName%></b> 입니다.
<p>
<hr/>
<jsp:include page="includeTagBottom.jsp">
	<jsp:param name="siteName" value="www.sdu.ac.kr" />
</jsp:include>
</body>
</html>