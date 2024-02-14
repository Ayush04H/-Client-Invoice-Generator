def PersonalBranding(services_selected):
    # Map the services to cost 
    service_cost = {service: 10 for service in services_selected}  # Assuming a dummy cost of 10 for each service
    
    # Create services_selected_in_markdown_format
    markdown_result = f"# Personal Branding\n\n| Service Component                   | Cost |\n|-------------------------------------|------|\n"

    for service in services_selected:
        markdown_result += f"| {service.ljust(35)} |  {service_cost[service]}  |\n"
    
    # Calculate Total cost
    total_cost = sum(service_cost.values())
    
    return markdown_result, total_cost


def ContentMarketing(services_selected):
    # Map the services to cost 
    service_cost = {service: 10 for service in services_selected}  # Assuming a dummy cost of 10 for each service
    
    # Create services_selected_in_markdown_format
    markdown_result = f"# Content Marketing\n\n| Service Component                   | Cost |\n|-------------------------------------|------|\n"

    for service in services_selected:
        markdown_result += f"| {service.ljust(35)} |  {service_cost[service]}  |\n"
    
    # Calculate Total cost
    total_cost = sum(service_cost.values())
    
    return markdown_result, total_cost


def LeadGeneration(services_selected):
    # Map the services to cost T
    service_cost = {service: 10 for service in services_selected}  # Assuming a dummy cost of 10 for each service
    
    # Create services_selected_in_markdown_format
    markdown_result = f"# Lead Generation\n\n| Service Component                   | Cost |\n|-------------------------------------|------|\n"

    for service in services_selected:
        markdown_result += f"| {service.ljust(35)} |  {service_cost[service]}  |\n"
    
    # Calculate Total cost
    total_cost = sum(service_cost.values())
    
    return markdown_result, total_cost


def WebDevelopment(services_selected):
    # Map the services to cost 
    service_cost = {service: 10 for service in services_selected}  # Assuming a dummy cost of 10 for each service
    
    # Create services_selected_in_markdown_format
    markdown_result = f"# Web Development\n\n| Service Component                   | Cost |\n|-------------------------------------|------|\n"

    for service in services_selected:
        markdown_result += f"| {service.ljust(35)} |  {service_cost[service]}  |\n"
    
    # Calculate Total cost
    total_cost = sum(service_cost.values())
    
    return markdown_result, total_cost
