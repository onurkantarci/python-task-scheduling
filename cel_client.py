from cel_main import TaskQueue, write_log

result = TaskQueue.delay("ZZZZZZZZZZZZZZZZZ")
print(result.get())

print(write_log.delay("The Logs Are Here>...!!").get())
