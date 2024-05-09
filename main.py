class Module:
    def __init__(self, module_id, module_type, version, parameters, mapper=None, metadata=None, flags=None):
        self.id = module_id
        self.module = module_type
        self.version = version
        self.parameters = parameters
        self.mapper = mapper
        self.metadata = metadata
        self.flags = flags

class Metadata:
    def __init__(self, designer, restore, parameters=None, interface=None, expect=None):
        self.designer = designer
        self.restore = restore
        self.parameters = parameters
        self.interface = interface
        self.expect = expect

class Designer:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Restore:
    def __init__(self, parameters=None, expect=None, extra=None):
        self.parameters = parameters
        self.expect = expect
        self.extra = extra

class Parameter:
    def __init__(self, name, param_type, label, required=False, validate=None):
        self.name = name
        self.type = param_type
        self.label = label
        self.required = required
        self.validate = validate

class Flow:
    def __init__(self, modules):
        self.modules = modules

class AppointmentSetterBot:
    def __init__(self, name, flow, metadata):
        self.name = name
        self.flow = Flow(flow)
        self.metadata = metadata

# Define each module
module_1 = Module(
    module_id=1,
    module_type="gateway:CustomWebHook",
    version=1,
    parameters={"hook": 472545, "maxResults": 1},
    mapper={},
    metadata=Metadata(
        designer=Designer(x=-1806, y=-140),
        restore=Restore(
            parameters={"hook": {"data": {"editable": "true"}, "label": "Appointment Setter"}},
            expect=None
        )
    )
)

# Define the flow
flow_modules = [module_1]  # Include other module instances as well

# Define the bot
appointment_setter_bot = AppointmentSetterBot(
    name="Appointment Setter Bot",
    flow=flow_modules,
    metadata=None  # Fill in metadata as required
)
