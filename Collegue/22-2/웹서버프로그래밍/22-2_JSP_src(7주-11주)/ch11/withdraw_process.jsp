<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ page import="java.sql.*" %>
<% 
	String u_id = request.getParameter("userID");
	String sql = "DELETE FROM members WHERE id = ?";
	
	String driverName="com.mysql.jdbc.Driver";
	String url = "jdbc:mysql://localhost:3306/odbo";
	String username = "root";
	String password = "123456";
	Connection conn = null;
	
	Class.forName(driverName);
	conn = DriverManager.getConnection(url, username, password);
	
	PreparedStatement prestm = conn.prepareStatement(sql);
	prestm.setString(1, u_id);

	int count = prestm.executeUpdate();
	
	if(count == 1){
		out.print("회원 탈퇴 성공!");
	}else{
		out.print("회원 탈퇴 실패!");
	}
	prestm.close();
	conn.close();	
%>