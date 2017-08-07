#coding=utf-8
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
	"""自定义权限，只有创建者才能编辑"""
	def has_object_permission(self, request, view, obj):
# Read permissions are allowed to any request,
# so we'll always allow GET, HEAD or OPTIONS requests.	
		if request.user.is_authenticated():
        # Do something for authenticated users.
			return True
		else:
 			return False
        # Do something for anonymous users.
		if request.method in permissions.SAFE_METHODS:
			return True
# Write permissions are only allowed to the owner of thesnippet.
		return obj.name == request.user