import psutil

def get_cpu_temp():
    temps = psutil.sensors_temperatures()

    if "coretemp" in temps:
        coretemps = temps['coretemp']

        package_temp = None
        core_values = []

        for t in coretemps:
            if "Package" in t.label:
                package_temp = t.current
            elif "Core" in t.label:
                core_values.append(t.current)
        
        if package_temp is not None:
            return package_temp
        
        if len(core_values) > 0:
            avg_cpu_temp = sum(core_values) / len(core_values)
            return avg_cpu_temp
    return None
