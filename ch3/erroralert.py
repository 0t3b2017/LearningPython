alert_system = 'console'
error_severity = 'critical'
error_message = 'OMG! Something happend!'
if alert_system == 'console':
    print(error_message)
elif alert_system == 'email':
    if error_severity == 'critical':
        send_email('admin@h3b.com.br', error_message)
    elif error_severity == 'medium':
        send_email('suporte@h3b.com.br', error_message)
    else:
        send_email('n1@h3b.com.br', error_message)
        
