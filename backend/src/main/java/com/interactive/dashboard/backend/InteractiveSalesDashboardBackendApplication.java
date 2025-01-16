package com.interactive.dashboard.backend;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.boot.autoconfigure.jdbc.DataSourceAutoConfiguration;

@SpringBootApplication(exclude = {DataSourceAutoConfiguration.class })
public class InteractiveSalesDashboardBackendApplication {

	public static void main(String[] args) {
		SpringApplication.run(InteractiveSalesDashboardBackendApplication.class, args);
	}

}
