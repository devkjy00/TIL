<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	   String siteName = request.getParameter("siteName");
%>
include 액션 태그와 param 액션 태그로 전달된 siteName은 
<font color="red"><%=siteName%></font> 입니다.
<hr/>